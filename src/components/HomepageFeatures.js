import React from 'react';
import clsx from 'clsx';
import styles from './HomepageFeatures.module.css';

const FeatureList = [
  {
    title: 'AI',
    Svg: require('../../img/ai.svg').default,
    description: (
      <>
        Galact is an ai, and works as a human-interactable abject when used. It can respond to humans in a fashion similar to human spech of moderen times.
      </>
    ),
  },
  {
    title: 'Easy to Use',
    Svg: require('../../static/img/logo.svg').default,
    description: (
      <>
        Galact is very easy to install and can be installed with pip, works like most other cli apps. It has a built in argument parser and works extensively with the use of argparse.
      </>
    ),
  },
  {
    title: 'CLI-Infused',
    Svg: require('../../static/img/cli.svg').default,
    description: (
      <>
        Galact works very well on a command line and can be easily used by anybody, due to simplistic installment and 
        easy and fast usage. It is even being planned to port to a gui! 
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} alt={title} />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
