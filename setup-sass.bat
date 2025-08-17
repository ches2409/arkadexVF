@echo off
echo ========================================
echo    ARKADEX - SASS SETUP SCRIPT
echo ========================================
echo.

echo [1/5] Verificando Node.js...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Node.js no esta instalado.
    echo Por favor instala Node.js desde: https://nodejs.org/
    pause
    exit /b 1
)
echo ✓ Node.js encontrado

echo.
echo [2/5] Instalando dependencias de SASS...
npm install
if %errorlevel% neq 0 (
    echo ERROR: Fallo la instalacion de dependencias
    pause
    exit /b 1
)
echo ✓ Dependencias instaladas

echo.
echo [3/5] Creando directorio CSS...
if not exist "static\css" mkdir "static\css"
echo ✓ Directorio CSS creado

echo.
echo [4/5] Compilando SASS por primera vez...
npm run build-css
if %errorlevel% neq 0 (
    echo ERROR: Fallo la compilacion de SASS
    pause
    exit /b 1
)
echo ✓ SASS compilado exitosamente

echo.
echo [5/5] Verificando archivos generados...
if exist "static\css\main.css" (
    echo ✓ main.css generado correctamente
) else (
    echo ERROR: main.css no fue generado
    pause
    exit /b 1
)

if exist "static\css\main.css.map" (
    echo ✓ Source map generado correctamente
) else (
    echo WARNING: Source map no fue generado
)

echo.
echo ========================================
echo        SETUP COMPLETADO ✓
echo ========================================
echo.
echo Comandos disponibles:
echo   npm run dev          - Modo desarrollo (watch)
echo   npm run build        - Compilar para produccion
echo   npm run build-css    - Compilar con source maps
echo   npm run check-sass   - Verificar sintaxis
echo.
echo Para iniciar el modo desarrollo:
echo   npm run dev
echo.
echo Archivo CSS generado en: static/css/main.css
echo Incluye este archivo en tu HTML en lugar del actual.
echo.
pause