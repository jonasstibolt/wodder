/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: [
    './mainapp/templates/**/*.html',
    './mainapp/static/wodder/**/*.css',
    // Add other paths as needed
  ],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')],
}

