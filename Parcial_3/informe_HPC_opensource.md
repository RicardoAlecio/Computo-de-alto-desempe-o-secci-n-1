# Informe técnico: Herramientas Open Source para Cómputo de Alto Desempeño (HPC)

**Tema:** Herramientas de código abierto para entornos de cómputo de alto desempeño  
**Autor:** [Tu nombre aquí]  
**Fecha:** 13 de May de 2025

## Introducción

El cómputo de alto desempeño (HPC, por sus siglas en inglés) es fundamental en campos como la ciencia de datos, simulaciones físicas, inteligencia artificial, genómica y modelado climático. Dado el costo elevado de las soluciones comerciales, muchas organizaciones recurren a herramientas *open source* para construir y administrar sus entornos HPC. 

Este informe presenta una selección de herramientas de código abierto clave que cubren diferentes aspectos del ecosistema HPC: sistemas operativos, administración de clústeres, programación paralela, gestión de trabajos, almacenamiento, monitoreo y portabilidad. El objetivo es proporcionar una visión general técnica y práctica de las soluciones más utilizadas y confiables en la comunidad científica y tecnológica.

## Clasificación de herramientas HPC open source

Las herramientas se agrupan en las siguientes categorías principales:

- Sistemas operativos y entornos base
- Gestores de trabajos y programación de tareas
- Bibliotecas de programación paralela
- Sistemas de archivos distribuidos
- Herramientas de monitoreo y visualización
- Contenedores y portabilidad

## Sistemas operativos y entornos base

### CentOS Stream / Rocky Linux / AlmaLinux

Estas distribuciones basadas en Red Hat son ampliamente utilizadas como sistema operativo en clústeres HPC debido a su estabilidad, soporte para herramientas científicas y compatibilidad con controladores de hardware.

- **CentOS Stream**: distribución rolling-release orientada a desarrollo.
- **Rocky Linux**: sucesor directo de CentOS, con enfoque en estabilidad.
- **AlmaLinux**: alternativa compatible con RHEL, mantenida por la comunidad.

## Gestores de trabajos y programación de tareas

### SLURM (Simple Linux Utility for Resource Management)

SLURM es el gestor de colas más popular en HPC. Permite la asignación eficiente de recursos en un clúster, la planificación de trabajos, el balanceo de carga y la gestión de prioridades.

- Alta escalabilidad
- Soporte para nodos heterogéneos
- Integración con MPI y bibliotecas científicas
- Interfaz por línea de comandos y API
- Plugins para contenedores, GPUs y más

### PBS (Portable Batch System)

PBS es otro sistema de gestión de colas utilizado en HPC. OpenPBS es su versión open source. Es común en ambientes académicos y científicos tradicionales.

- Gestión de trabajos basada en scripts
- Control de políticas de usuario
- Compatibilidad con otros middleware como Torque
- Escalabilidad probada en centros de investigación

## Bibliotecas de programación paralela

### MPI (Message Passing Interface)

MPI es el estándar de facto para programación paralela distribuida. Existen varias implementaciones open source:

- **OpenMPI**
- **MPICH**

Características:

- Comunicación entre procesos en diferentes nodos
- Escalabilidad a miles de nodos
- Uso extensivo en simulaciones científicas
- Soporte para redes de alta velocidad como Infiniband

### OpenMP

OpenMP es un estándar para paralelismo compartido (multi-threading) en memoria compartida, utilizado principalmente en CPU multicore.

- Directivas en código C, C++ y Fortran
- Fácil de implementar sobre código existente
- Complementario a MPI
- Ideal para optimización de código en CPUs modernas

## Sistemas de archivos distribuidos

### Lustre

Sistema de archivos distribuido diseñado para HPC, optimizado para I/O masivo en entornos de múltiples nodos.

- Soporta petabytes de datos
- Alto rendimiento en clústeres grandes
- Utilizado en supercomputadoras del DOE (Department of Energy)
- Ideal para cargas de trabajo con acceso concurrente intensivo

### BeeGFS

Sistema de archivos distribuido más fácil de implementar que Lustre, con buen rendimiento para cargas mixtas.

- Escalabilidad modular
- Alta disponibilidad
- Adecuado para clústeres medianos y pequeños
- Administración centralizada por GUI o CLI

## Herramientas de monitoreo y visualización

### Ganglia

Sistema de monitoreo distribuido escalable para clústeres y grids. Permite visualizar métricas en tiempo real.

- Monitoreo de CPU, memoria, red, carga
- Basado en RRDTool y XML
- Interfaz web intuitiva
- Ligero y eficiente

### Grafana + Prometheus

Plataforma moderna de monitoreo y visualización.

- Recolección de métricas con Prometheus
- Paneles personalizables en Grafana
- Adecuado para integraciones avanzadas
- Alerta basada en condiciones y métricas específicas

## Contenedores y portabilidad

### Singularity (Apptainer)

Herramienta de contenedores diseñada específicamente para entornos HPC. A diferencia de Docker, permite integrarse de forma segura con entornos multiusuario.

- Compatible con imágenes Docker
- Integración con sistemas de archivos compartidos
- Ejecución sin privilegios de root
- Reproducibilidad de entornos científicos

### Charliecloud

Alternativa ligera para ejecutar contenedores sin privilegios en entornos HPC.

- Aislamiento por usuario
- Compatible con CI/CD y builds reproducibles
- Diseñado para simplicidad y seguridad en clústeres académicos

## Casos de uso reales

- **NASA** y **NOAA** utilizan SLURM, Lustre y MPI para modelado climático y análisis satelital.
- **CERN** integra OpenMPI y SLURM para simulaciones de partículas subatómicas.
- Universidades como **MIT**, **Stanford** y el **ITAM** han adoptado Singularity para reproducibilidad en investigación científica.
- Centros de supercómputo como el *Oak Ridge National Laboratory* emplean herramientas como BeeGFS, Prometheus y OpenMPI para mantener sus infraestructuras.

## Conclusión

Las herramientas open source para cómputo de alto desempeño constituyen una base sólida para construir infraestructuras robustas, eficientes y escalables. Gracias a la comunidad científica y tecnológica, existe un ecosistema maduro de soluciones que permiten a instituciones académicas, centros de investigación y empresas acceder a tecnologías avanzadas sin incurrir en altos costos de licencias.

Al seleccionar herramientas open source para HPC, es fundamental considerar el tamaño del clúster, los requisitos de software, la experiencia del equipo técnico y la necesidad de soporte a largo plazo. El uso combinado de SLURM, MPI, sistemas de archivos distribuidos como Lustre o BeeGFS y herramientas de monitoreo modernas garantiza un entorno productivo y competitivo.
