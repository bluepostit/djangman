var path = require("path")
var webpack = require("webpack")
var BundleTracker = require("webpack-bundle-tracker");

module.exports = {
    context: __dirname,
    entry: './assets/js/index.js',
    output: {
        path: path.resolve('./assets/bundles/'),
        filename: "[name]-[hash].js",
    },
    mode: "development",
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
    ],
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [ "style-loader", "css-loader" ]
            }
        ]
    }
}