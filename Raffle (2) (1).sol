// SPDX-License-Identifier: MIT
//source: https://spaceofmatej.com/build-a-raffle-system-in-solidity
pragma solidity ^0.8.0;
contract Raffle {
    address[] contestants;
//not truly random using block.prevrando: https://stackoverflow.com/questions/48848948/how-to-generate-a-random-number-in-solidity
    
    function PickWinner() private view returns (uint) {
        uint random = uint(keccak256(abi.encodePacked(block.difficulty, block.timestamp, contestants)));
        uint index = random % contestants.length;
        return index;
    }
    
    function EnterRaffle() public payable{
        require(msg.value == 2 ether, "pay 2 ether to enter the raffle ");
        contestants.push(msg.sender);
        if (contestants.length >=3) {
            uint winnerIndex = PickWinner();
            address winner = contestants[winnerIndex];
            uint prizeAmount = address(this).balance;
            (bool success, ) = (winner).call{value: prizeAmount}("");
            require (success, "failed to withdraw money from the contract");
            delete contestants;
        }
    }
    
    function getLength() public view returns (uint) {
        return contestants.length;
    }
}

