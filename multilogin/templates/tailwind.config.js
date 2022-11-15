/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./index.html', 
    "/static/app/**/*.{html,js}",
    ],
    theme: {
      extend: {},
    },
    plugins: [
      require('@tailwindcss/forms'),
    ],
  }