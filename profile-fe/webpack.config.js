const path = require('path')
const BundleTracker = require('webpack-bundle-tracker')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')

module.exports = {
  entry: {
    staticfiles: './src/index.js',
  },
  output: {
    path: path.resolve('../profile_be/static/'),
    filename: '[name]-[fullhash].js',
    publicPath: 'static/',
    clean: true
  },
  plugins: [
    new CleanWebpackPlugin(),
    new BundleTracker({
      path: __dirname,
      filename: './webpack-stats.json',
    }),
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ['babel-loader'],
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
      {
            test: /\.(png|jpg|svg|pdf|ttf)$/i,
            type: 'asset'
        }
    ],
  },
}