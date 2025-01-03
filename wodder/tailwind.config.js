/** @type {import('tailwindcss').Config} */
module.exports = {
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

