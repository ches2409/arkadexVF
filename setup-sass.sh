#!/bin/bash

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}    ARKADEX - SASS SETUP SCRIPT${NC}"
echo -e "${BLUE}========================================${NC}"
echo

echo -e "${YELLOW}[1/5] Verificando Node.js...${NC}"
if ! command -v node &> /dev/null; then
    echo -e "${RED}ERROR: Node.js no está instalado.${NC}"
    echo -e "${RED}Por favor instala Node.js desde: https://nodejs.org/${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Node.js encontrado$(NC)"

echo
echo -e "${YELLOW}[2/5] Instalando dependencias de SASS...${NC}"
if ! npm install; then
    echo -e "${RED}ERROR: Falló la instalación de dependencias${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Dependencias instaladas${NC}"

echo
echo -e "${YELLOW}[3/5] Creando directorio CSS...${NC}"
mkdir -p static/css
echo -e "${GREEN}✓ Directorio CSS creado${NC}"

echo
echo -e "${YELLOW}[4/5] Compilando SASS por primera vez...${NC}"
if ! npm run build-css; then
    echo -e "${RED}ERROR: Falló la compilación de SASS${NC}"
    exit 1
fi
echo -e "${GREEN}✓ SASS compilado exitosamente${NC}"

echo
echo -e "${YELLOW}[5/5] Verificando archivos generados...${NC}"
if [ -f "static/css/main.css" ]; then
    echo -e "${GREEN}✓ main.css generado correctamente${NC}"
else
    echo -e "${RED}ERROR: main.css no fue generado${NC}"
    exit 1
fi

if [ -f "static/css/main.css.map" ]; then
    echo -e "${GREEN}✓ Source map generado correctamente${NC}"
else
    echo -e "${YELLOW}WARNING: Source map no fue generado${NC}"
fi

echo
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}        SETUP COMPLETADO ✓${NC}"
echo -e "${GREEN}========================================${NC}"
echo
echo -e "${BLUE}Comandos disponibles:${NC}"
echo -e "  ${YELLOW}npm run dev${NC}          - Modo desarrollo (watch)"
echo -e "  ${YELLOW}npm run build${NC}        - Compilar para producción"
echo -e "  ${YELLOW}npm run build-css${NC}    - Compilar con source maps"
echo -e "  ${YELLOW}npm run check-sass${NC}   - Verificar sintaxis"
echo
echo -e "${BLUE}Para iniciar el modo desarrollo:${NC}"
echo -e "  ${YELLOW}npm run dev${NC}"
echo
echo -e "${BLUE}Archivo CSS generado en:${NC} static/css/main.css"
echo -e "${BLUE}Incluye este archivo en tu HTML en lugar del actual.${NC}"
echo