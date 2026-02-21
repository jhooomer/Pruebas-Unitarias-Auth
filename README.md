# Pruebas-Unitarias-Auth

# Módulo de Autenticación - Pruebas Unitarias (Ingeniería de Software)

Este repositorio contiene la implementación de pruebas unitarias para el módulo de autenticación de usuarios, diseñado bajo los lineamientos de aseguramiento de calidad y gestión de riesgos.

## 1. Propósito de las Pruebas
El objetivo principal es validar la lógica de negocio del sistema de acceso, garantizando que las funciones de autenticación respondan correctamente ante diferentes escenarios de uso y ataques potenciales.

## 2. Relación con los Casos de Uso
Basado en el diseño previo, se han cubierto los siguientes escenarios:

* **Caso de Uso 1: Validación de Credenciales**
    * [cite_start]`test_login_success`: Verifica que el acceso sea concedido con credenciales válidas[cite: 1, 10].
    * [cite_start]`test_login_wrong_password`: Valida que el sistema rechace el acceso con credenciales incorrectas, garantizando la integridad.
* **Caso de Uso 2: Política de Seguridad (Bloqueo)**
    * [cite_start]`test_account_locking_after_3_attempts`: Implementa la validación de la contramedida ante riesgos de fuerza bruta (bloqueo tras 3 intentos fallidos), alineado con la **Gestión de Riesgos** del Plan de Pruebas[cite: 2, 3].

## 3. Alineación con SQA (Aseguramiento de Calidad)
Siguiendo el **SQA Checklist** proporcionado:
* [cite_start]**Gestión de Riesgos**: Se implementaron pruebas específicas para las contramedidas de seguridad definidas[cite: 3].
* [cite_start]**Revisión de Producto**: Estas pruebas unitarias representan la actividad de revisión técnica del producto de trabajo (Work Product)[cite: 10].
* [cite_start]**Monitoreo**: Los resultados de `pytest` sirven como métricas de éxito para la liberación del módulo[cite: 7].

## 4. Requisitos e Instalación
Para ejecutar las pruebas localmente, asegúrese de tener Python instalado y siga estos pasos:

1. Instalar el framework de pruebas:
   ```bash
   pip install pytest
