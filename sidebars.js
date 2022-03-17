module.exports = {
    sidebars: [
    'intro',
    {
        type: 'category',
        label: 'Getting Started',
        link: {
          type: 'generated-index',
          title: 'Get Started with Galact',
          description: "Begin using galact in your system.",
        },
        collapsed: false,
        items: [
          'installation',
          'usage',
        ],
      },
      'why',
    ],
  };