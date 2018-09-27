const path = require('path');

module.exports = {
    entry: './project/ifap/static/ifap/js/src/index.js',
    output: {
        filename: "build.js",
        path: path.resolve(__dirname, "project/ifap/static/ifap/js")
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            }
        ]
    },
    mode: "development"
};