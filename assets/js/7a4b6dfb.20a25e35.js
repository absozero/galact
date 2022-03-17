"use strict";(self.webpackChunkgalact_docs=self.webpackChunkgalact_docs||[]).push([[609],{3905:function(e,t,n){n.d(t,{Zo:function(){return l},kt:function(){return m}});var r=n(7294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function c(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var u=r.createContext({}),s=function(e){var t=r.useContext(u),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},l=function(e){var t=s(e.components);return r.createElement(u.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},g=r.forwardRef((function(e,t){var n=e.components,a=e.mdxType,o=e.originalType,u=e.parentName,l=c(e,["components","mdxType","originalType","parentName"]),g=s(n),m=a,d=g["".concat(u,".").concat(m)]||g[m]||p[m]||o;return n?r.createElement(d,i(i({ref:t},l),{},{components:n})):r.createElement(d,i({ref:t},l))}));function m(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=n.length,i=new Array(o);i[0]=g;var c={};for(var u in t)hasOwnProperty.call(t,u)&&(c[u]=t[u]);c.originalType=e,c.mdxType="string"==typeof e?e:a,i[1]=c;for(var s=2;s<o;s++)i[s]=n[s];return r.createElement.apply(null,i)}return r.createElement.apply(null,n)}g.displayName="MDXCreateElement"},4182:function(e,t,n){n.r(t),n.d(t,{assets:function(){return l},contentTitle:function(){return u},default:function(){return m},frontMatter:function(){return c},metadata:function(){return s},toc:function(){return p}});var r=n(3117),a=n(102),o=(n(7294),n(3905)),i=["components"],c={slug:"release-docs",title:"Releasing docs website using Docusaurus",authors:{name:"Absozero",title:"Galact maintainer, original author",url:"https://github.com/absozero",image_url:"https://github.com/absozero.png"},tags:["Galact","Documentation"]},u=void 0,s={permalink:"/galact/blog/release-docs",editUrl:"https://github.com/absozero/galact/tree/documentation/blog/2021-11-28-docs-docusaurus.md",source:"@site/blog/2021-11-28-docs-docusaurus.md",title:"Releasing docs website using Docusaurus",description:"When I started Galact, I knew that I had to make good documentation to help users",date:"2021-11-28T00:00:00.000Z",formattedDate:"November 28, 2021",tags:[{label:"Galact",permalink:"/galact/blog/tags/galact"},{label:"Documentation",permalink:"/galact/blog/tags/documentation"}],readingTime:.48,truncated:!1,authors:[{name:"Absozero",title:"Galact maintainer, original author",url:"https://github.com/absozero",image_url:"https://github.com/absozero.png",imageURL:"https://github.com/absozero.png"}],frontMatter:{slug:"release-docs",title:"Releasing docs website using Docusaurus",authors:{name:"Absozero",title:"Galact maintainer, original author",url:"https://github.com/absozero",image_url:"https://github.com/absozero.png",imageURL:"https://github.com/absozero.png"},tags:["Galact","Documentation"]},prevItem:{title:"Migrating Galact to a cli structure for scalability",permalink:"/galact/blog/setup-cli"}},l={authorsImageUrls:[void 0]},p=[],g={toc:p};function m(e){var t=e.components,n=(0,a.Z)(e,i);return(0,o.kt)("wrapper",(0,r.Z)({},g,n,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("p",null,"When I started Galact, I knew that I had to make good documentation to help users\nunderstand the project, and I knew that I could just make a wiki on the github wiki and\nbe done and move on. But I also knew that I could do better and decided to make a website for the\npiece of software, and then I eventually landed on Docusaurus. It was like a CMS but with similar capabilities and less difficulties."),(0,o.kt)("p",null,"So I decided to set up a website for Galact. This is what you are seeing right now."))}m.isMDXComponent=!0}}]);