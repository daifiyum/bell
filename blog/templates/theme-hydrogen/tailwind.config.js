/** @type {import('tailwindcss').Config} */
const { addDynamicIconSelectors } = require('@iconify/tailwind');

module.exports = {
  content: ["./**/*.html", "./source/js/core.js"],
  theme: {
    extend: {
      lineHeight: {
        'compact': '0.5',
      },
      transition: {
        'moreAn': 'transform .25s cubic-bezier(.4,0,.2,1),opacity 125ms 125ms;'
      },
      backgroundColor: {
        'hover': '#0000000d',
        'active': '#0000001a'
      },
      colors: {
        'icon': '#626262',
      },
      fontSize: {
        'title': '1.125rem',
      },
      boxShadow: {
        'inner1': 'inset 0px 0px 2px 2px rgb(0 0 0 / 0.05)',
      }
    },
  },
  darkMode: 'class',
  plugins: [
    addDynamicIconSelectors(),
    require("@tailwindcss/typography")
  ],
}