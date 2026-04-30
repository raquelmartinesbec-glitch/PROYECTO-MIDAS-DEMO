# ══════════════════════════════════════════════════════════════════════════════
# test_config.py - Tests de configuración y despliegue
# Validación de archivos de configuración y setup del proyecto
# ══════════════════════════════════════════════════════════════════════════════

import pytest
import os
import toml
import yaml
import json
import subprocess
import sys
from pathlib import Path


class TestProjectStructure:
    """Tests para validar la estructura profesional del proyecto"""
    
    def test_professional_directory_structure(self):
        """Verificar estructura de directorios siguiendo mejores prácticas"""
        project_root = Path(__file__).parent.parent
        
        # Directorios que deben existir según reorganización enterprise
        expected_dirs = [
            "src",
            "src/dashboard", 
            "config",
            "docs",
            "scripts", 
            "tests",
            "docker",
            "requirements"
        ]
        
        for dir_name in expected_dirs:
            dir_path = project_root / dir_name
            assert dir_path.exists(), f"Directorio faltante: {dir_name}"
            assert dir_path.is_dir(), f"{dir_name} no es un directorio"
            
        print("✅ Estructura de directorios enterprise OK")
        
    def test_critical_files_exist(self):
        """Verificar que existan archivos críticos del proyecto"""
        project_root = Path(__file__).parent.parent
        
        critical_files = [
            "pyproject.toml",           # Configuración moderna Python
            "README.md",                # Documentación principal  
            "config/railway.toml",      # Configuración Railway
            "docker/Dockerfile",        # Containerización
            "src/dashboard/app.py",     # Dashboard principal
            "requirements/requirements.txt",  # Dependencias
            "docs/README.md",          # Documentación organizada
            "scripts/run_local.py",    # Script de ejecución local
        ]
        
        for file_path in critical_files:
            full_path = project_root / file_path
            assert full_path.exists(), f"Archivo crítico faltante: {file_path}"
            assert full_path.is_file(), f"{file_path} no es un archivo"
            
        print("✅ Archivos críticos presentes")
        
    def test_obsolete_files_removed(self):
        """Verificar que archivos obsoletos fueron eliminados"""
        project_root = Path(__file__).parent.parent
        
        # Archivos que NO deben existir después de la reorganización
        obsolete_files = [
            "run_demo.py",
            "simple_demo_api.py",
            "test_demo_api.py",
            "test_simple_demo.py",
            "midas_dashboard.py",
            "demo_dashboard/demo_app.py",
            "demo_api/demo_main.py"
        ]
        
        for file_path in obsolete_files:
            full_path = project_root / file_path
            assert not full_path.exists(), f"Archivo obsoleto aún presente: {file_path}"
            
        print("✅ Archivos obsoletos eliminados correctamente")


class TestConfigurationFiles:
    """Tests para archivos de configuración"""
    
    def test_pyproject_toml_valid(self):
        """Validar configuración pyproject.toml"""
        project_root = Path(__file__).parent.parent
        pyproject_path = project_root / "pyproject.toml"
        
        assert pyproject_path.exists(), "pyproject.toml faltante"
        
        # Cargar y validar contenido
        with open(pyproject_path) as f:
            config = toml.load(f)
            
        # Verificar secciones críticas
        assert "project" in config, "Sección [project] faltante"
        assert "build-system" in config, "Sección [build-system] faltante"
        
        project_config = config["project"]
        assert "name" in project_config, "Nombre del proyecto faltante"
        assert "version" in project_config, "Versión faltante"
        assert "dependencies" in project_config, "Dependencies faltante"
        
        # Verificar dependencias críticas
        dependencies = project_config["dependencies"]
        required_deps = ["streamlit", "plotly", "pandas"]
        
        for dep in required_deps:
            assert any(dep in d for d in dependencies), f"Dependencia faltante: {dep}"
            
        print("✅ pyproject.toml válido")
        
    def test_railway_config_valid(self):
        """Validar configuración Railway"""
        project_root = Path(__file__).parent.parent
        railway_configs = [
            "config/railway.toml",
            "railway.toml"
        ]
        
        valid_config_found = False
        
        for config_path in railway_configs:
            full_path = project_root / config_path
            if full_path.exists():
                with open(full_path) as f:
                    content = f.read()
                    
                # Verificar contenido crítico
                assert "startCommand" in content or "[deploy]" in content, "Configuración Railway incompleta"
                if "streamlit run" in content:
                    valid_config_found = True
                    
        assert valid_config_found, "No se encontró configuración Railway válida"
        print("✅ Configuración Railway válida")
        
    def test_docker_config_valid(self):
        """Validar configuración Docker"""
        project_root = Path(__file__).parent.parent
        dockerfile_path = project_root / "docker" / "Dockerfile"
        
        if dockerfile_path.exists():
            with open(dockerfile_path) as f:
                content = f.read()
                
            # Verificar instrucciones básicas
            assert "FROM python:" in content, "FROM instruction faltante o incorrecta"
            assert "COPY" in content, "COPY instruction faltante" 
            assert "RUN pip install" in content or "requirements" in content, "Instalación dependencias faltante"
            assert "CMD" in content or "ENTRYPOINT" in content, "Comando de inicio faltante"
            
            print("✅ Dockerfile válido")
        else:
            pytest.skip("Dockerfile no encontrado - OK para proyecto simple")
            
    def test_requirements_valid(self):
        """Validar archivo requirements.txt"""
        project_root = Path(__file__).parent.parent
        req_files = [
            "requirements/requirements.txt",
            "requirements.txt"
        ]
        
        requirements_found = False
        
        for req_file in req_files:
            full_path = project_root / req_file
            if full_path.exists():
                with open(full_path) as f:
                    content = f.read().lower()
                    
                # Verificar dependencias críticas
                required_packages = ["streamlit", "plotly", "pandas"]
                for package in required_packages:
                    assert package in content, f"Dependencia crítica faltante: {package}"
                    
                requirements_found = True
                break
                
        assert requirements_found, "Archivo requirements.txt no encontrado"
        print("✅ requirements.txt válido")


class TestDocumentation:
    """Tests para documentación del proyecto"""
    
    def test_readme_comprehensive(self):
        """Verificar que README.md sea comprehensivo"""
        project_root = Path(__file__).parent.parent
        readme_path = project_root / "README.md"
        
        assert readme_path.exists(), "README.md faltante"
        
        with open(readme_path, encoding='utf-8') as f:
            content = f.read().lower()
            
        # Secciones que debe contener
        expected_sections = [
            "midas",
            "instalación" or "install",
            "uso" or "cómo usar",
            "configuración" or "config", 
            "estructura" or "architecture",
            "despliegue" or "deploy"
        ]
        
        section_found = []
        for section in expected_sections:
            if section in content:
                section_found.append(section)
                
        assert len(section_found) >= 4, f"README incompleto. Secciones encontradas: {section_found}"
        print("✅ README.md comprehensivo")
        
    def test_changelog_exists(self):
        """Verificar que exista historial de cambios"""
        project_root = Path(__file__).parent.parent
        changelog_paths = [
            "docs/CHANGELOG.md",
            "CHANGELOG.md"
        ]
        
        changelog_found = False
        for path in changelog_paths:
            if (project_root / path).exists():
                changelog_found = True
                break
                
        assert changelog_found, "CHANGELOG.md no encontrado"
        print("✅ Historial de cambios documentado")


class TestScripts:
    """Tests para scripts de automatización"""
    
    def test_run_local_script_valid(self):
        """Validar script de ejecución local"""
        project_root = Path(__file__).parent.parent
        script_path = project_root / "scripts" / "run_local.py"
        
        if script_path.exists():
            # Verificar sintaxis Python
            result = subprocess.run([
                sys.executable, '-m', 'py_compile', str(script_path)
            ], capture_output=True)
            
            assert result.returncode == 0, f"Error de sintaxis en run_local.py: {result.stderr.decode()}"
            
            # Verificar que contenga lógica de Streamlit
            with open(script_path) as f:
                content = f.read()
                
            assert "streamlit" in content.lower(), "Script no contiene referencia a Streamlit"
            print("✅ Script run_local.py válido")
        else:
            pytest.skip("Script run_local.py no encontrado")
            
    def test_deploy_script_valid(self):
        """Validar script de despliegue"""
        project_root = Path(__file__).parent.parent
        script_paths = [
            "scripts/deploy.sh",
            "deploy.sh"
        ]
        
        script_found = False
        for script_path in script_paths:
            full_path = project_root / script_path
            if full_path.exists():
                with open(full_path) as f:
                    content = f.read()
                    
                # Verificar comandos básicos de deploy
                expected_commands = ["git", "railway", "docker"]
                command_found = any(cmd in content.lower() for cmd in expected_commands)
                
                assert command_found, "Script de deploy no contiene comandos esperados"
                script_found = True
                break
                
        if script_found:
            print("✅ Script de despliegue válido")
        else:
            pytest.skip("Script de despliegue no encontrado - OK para proyecto simple")


class TestEnvironment:
    """Tests de configuración del entorno"""
    
    def test_python_version_compatibility(self):
        """Verificar compatibilidad de versión Python"""
        project_root = Path(__file__).parent.parent
        
        # Verificar .python-version si existe
        python_version_file = project_root / ".python-version"
        if python_version_file.exists():
            with open(python_version_file) as f:
                version = f.read().strip()
                
            # Debe ser Python 3.9+ según pyproject.toml
            major, minor = map(int, version.split('.')[:2])
            assert major >= 3 and minor >= 9, f"Versión Python demasiado antigua: {version}"
            print(f"✅ Python {version} compatible")
        else:
            # Verificar versión actual
            current_version = sys.version_info
            assert current_version >= (3, 9), f"Python {current_version.major}.{current_version.minor} demasiado antiguo"
            print(f"✅ Python {current_version.major}.{current_version.minor}.{current_version.micro} compatible")
            
    def test_env_example_exists(self):
        """Verificar que exista archivo de variables de entorno de ejemplo"""
        project_root = Path(__file__).parent.parent
        env_paths = [
            ".env.example",
            "config/.env.example" 
        ]
        
        env_example_found = False
        for path in env_paths:
            if (project_root / path).exists():
                env_example_found = True
                break
                
        assert env_example_found, "Archivo .env.example no encontrado"
        print("✅ Configuración de entorno documentada")


if __name__ == "__main__":
    print("⚙️  Ejecutando tests de configuración MIDAS...")
    
    # Test estructura
    print("\n📁 Verificando estructura enterprise...")
    try:
        test_structure = TestProjectStructure()
        test_structure.test_professional_directory_structure()
        test_structure.test_critical_files_exist()
        test_structure.test_obsolete_files_removed()
    except Exception as e:
        print(f"❌ Error en estructura: {e}")
        
    # Test configuración
    print("\n⚙️ Verificando configuraciones...")
    try:
        test_config = TestConfigurationFiles()
        test_config.test_pyproject_toml_valid()
        test_config.test_railway_config_valid()
        test_config.test_requirements_valid()
    except Exception as e:
        print(f"❌ Error en configuración: {e}")
        
    # Test documentación
    print("\n📚 Verificando documentación...")
    try:
        test_docs = TestDocumentation()
        test_docs.test_readme_comprehensive()
        test_docs.test_changelog_exists()
    except Exception as e:
        print(f"❌ Error en documentación: {e}")
        
    print("\n🎯 Tests de configuración completados.")