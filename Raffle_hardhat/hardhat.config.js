require("hardhat-deploy");
require("dotenv").config();
require("@nomiclabs/hardhat-waffle");

/**
 * @type import('hardhat/config').HardhatUserConfig
 */

module.exports = {
  solidity: "0.8.7",
  networks: {
    goerli: {
      url: "https://goerli.infura.io/v3/${process.env.GOERLI_URL_API}", //Infura url with projectId
      accounts: ["${process.env.WALLET_PRIVATE_KEY}"] // add the account that will deploy the contract (private key)
    },
  },
  namedAccounts: {
    deployer: {
      default: 0
    },
  }
};