// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Galact-docs',
  tagline: 'Get to galaxies with Galact!',
  url: 'https://absozero.github.io',
  baseUrl: '/galact/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'absozero', // Usually your GitHub org/user name.
  projectName: 'galact', // Usually your repo name.
  plugins: [require.resolve("@cmfcmf/docusaurus-search-local")],

  presets: [
    [
      '@docusaurus/preset-classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          
          editUrl: 'https://github.com/absozero/galact/tree/documentation/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/absozero/galact/tree/documentation/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    ({
    colorMode: {
        defaultMode: 'dark',
    },
      navbar: {
        hideOnScroll: true,
        title: 'Galact',
        logo: {
          alt: 'Galact Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'doc',
            docId: 'intro',
            position: 'left',
            label: 'Docs',
          },

          {
            to: '/blog',
            label: 'Blog',
            position: 'left'
          },

          {
            to: '/about/about',
            position: 'right',
            label: 'About'
          },
          {
            href: 'https://github.com/absozero/galact',
            position: 'right',
            label: 'GitHub',
            className: 'header-item-github',
            'aria-label': 'GitHub repository',
          },
          
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Docs',
                to: '/docs/intro',
              },
            ],
          },
          {
            title: 'Links',
            items: [
              {
                label: 'Github Repo',
                href: 'https://github.com/absozero/galact',
                                
              },
              {
                  label: 'Absozero',
                  href: 'https://absozero.github.io',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'Blog',
                to: '/blog',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/absozero/galact',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} absozero`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
