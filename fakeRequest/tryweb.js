const Tryweb = require("tryweb");
const trywebDOM = require("tryweb-dom");

const App = () => {
  return (
    <webView>
      <trycode>Tryweb.front.br</trycode>
      <trycode>Tryweb.front.startcenter</trycode>
      <trycode>Tryweb.front.h2("Hello")</trycode>
      <trycode>Tryweb.front.endcenter</trycode>
    </webView>
  );
};

result = trywebDOM.complie(App());
trywebDOM.render(result);

// npx tryweb <mainfile.js>