/** @type {import('tailwindcss').Config} */
module.exports = {
  
  content: [
    "./dist/*.{html,js}",
    "../templates/*.html" /** templates in base */,
    "../*/templates/*/*.html" /** templates in applications */
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
