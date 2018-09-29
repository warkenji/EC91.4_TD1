const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = [{
    name: "ifap",
    devtool: 'inline-source-map',
    entry: {
        bundle: [
            './project/ifap/assets/ts/main.ts',
            './project/ifap/assets/scss/main.scss'
        ]
    },
    output: {
        filename: "js/[name].js",
        path: path.resolve(__dirname, "project/ifap/static/ifap")
    },
    module: {
        rules: [
            {
                test: /\.ts$/,
                use: 'ts-loader',
                exclude: /node_modules/
            },
            {
                test: /\.scss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    "css-loader",
                    "sass-loader"
                ]
            }
        ]
    }
    ,
    resolve: {
        extensions: [ '.ts', '.js' ]
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: "css/[name].css"
        })
    ],
    mode: "development"
}];