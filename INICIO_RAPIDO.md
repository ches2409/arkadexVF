# 🚀 Inicio Rápido - SASS con SMACSS

## ⚡ Configuración en 3 pasos

### 1. Ejecutar script de configuración

**En Windows:**
```bash
# Hacer doble clic en el archivo o ejecutar en terminal:
setup-sass.bat
```

**En Linux/Mac:**
```bash
# Dar permisos de ejecución y ejecutar:
chmod +x setup-sass.sh
./setup-sass.sh
```

### 2. Incluir CSS compilado en tu HTML

Reemplaza en tu archivo `layout.html` o template principal:

```html
<!-- ❌ Reemplazar esto -->
<link rel="stylesheet" href="{{ url_for('static', filename='main.css') }}">

<!-- ✅ Con esto -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
```

### 3. Iniciar modo desarrollo

```bash
npm run dev
```

¡Listo! Ahora cualquier cambio en los archivos `.scss` se compilará automáticamente.

---

## 📁 Archivos importantes creados

- `📄 SASS_SMACSS_GUIDE.md` - Guía completa y detallada
- `📦 package.json` - Configuración de npm y scripts
- `⚙️ .sassrc` - Configuración de SASS
- `🚫 .gitignore` - Archivos a ignorar en git
- `🔧 setup-sass.bat/sh` - Scripts de configuración automática

---

## 🎯 Comandos principales

```bash
# Desarrollo (recompila automáticamente)
npm run dev

# Compilar una vez
npm run build-css

# Compilar para producción (comprimido)
npm run build

# Verificar sintaxis
npm run check-sass
```

---

## 🎨 Personalización rápida

### Cambiar colores del tema
Edita `static/scss/abstracts/_variables.scss`:

```scss
// Colores principales
$primary-color: #00d4ff;    // Azul neón
$accent-pink: #ff0080;      // Rosa neón
$accent-green: #00ff88;     // Verde neón
$accent-yellow: #ffff00;    // Amarillo neón
```

### Agregar nuevos componentes
1. Crear archivo en `static/scss/components/_mi-componente.scss`
2. Agregar `@import 'scss/components/mi-componente';` en `style.scss`
3. Compilar con `npm run build-css`

---

## 🔧 Solución de problemas comunes

### Error: "Node.js no encontrado"
**Solución:** Instalar Node.js desde https://nodejs.org/

### Error: "sass command not found"
**Solución:** 
```bash
npm install -g sass
# o usar el script local:
npm run build-css
```

### Los estilos no se aplican
**Solución:** Verificar que el HTML incluya el CSS correcto:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
```

### Cambios no se reflejan
**Solución:** 
1. Verificar que el modo watch esté activo: `npm run dev`
2. Refrescar el navegador (Ctrl+F5)
3. Verificar la consola del navegador por errores

---

## 📚 Próximos pasos

1. **Leer la guía completa:** `SASS_SMACSS_GUIDE.md`
2. **Personalizar variables:** Editar `_variables.scss`
3. **Crear componentes:** Agregar archivos en `components/`
4. **Usar utilidades:** Aplicar clases como `.text-primary`, `.m-4`, `.flex`
5. **Optimizar:** Usar `npm run build` para producción

---

**¡Tu proyecto ahora tiene un sistema de estilos profesional y escalable! 🎉**