var markdownpdf = require("markdown-pdf")

var options = { 
    remarkable: {
        html: true,
        breaks: true,
        plugins: [ require('remarkable-classy') ]
    }
}

markdownpdf(options)
  .from("./README.md")
  .to("./README.pdf", function () { console.log("Done") })