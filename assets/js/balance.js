
class Player {
	constructor(nickname, pts) {
		this.nickname = nickname;
		this.pts = pts;
	}
}

class Game {
	constructor(players1, players2) {
		this.players = [players1, players2];
		this.sum = [0, 0];
		this.avg = [0, 0];
		var groupsVol = this.players[0].length;
		for (var i = 0; i < groupsVol; i++){
			this.sum[0] += players1[i].pts;
			this.sum[1] += players2[i].pts;
		}
		this.avg[0] = Math.round(this.sum[0] / groupsVol);
		this.avg[1] = Math.round(this.sum[1] / groupsVol);
	}

	/*get fullGame(){
		var players1 = [];
		var players2 = [];
		var groupsVol = 5;
		for (var i = 0; i < groupsVol; i++){

		}

	}
	*/
}

function getRandomArbitrary(min, max) {
  return Math.random() * (max - min) + min;
}

function div(val, by) {
		return (val - val % by) / by;
}

function comparePlayersPts(a,b){
	return a.pts - b.pts;
}

function winLoseCosts(avg1,avg2) {
	var winPrice = 50;
	var cost = Math.round(avg2 * 100 / avg1) / 100;
	return Math.round((winPrice / 2) * cost);
}

function splitPlayers(allPlayers) {
	var groupsVol = 5;
	var players1 = [];
	var players2 = [];
	var sum1 = 0;
	var sum2 = 0;

	while ((players1.length < groupsVol) || (players2.length < groupsVol)) {
		var players = allPlayers.sort(comparePlayersPts);
		var player = players.pop();
		if ((sum1 <= sum2) && (players1.length < groupsVol)) {
			players1.push(player);
			sum1 += player.pts;
		}
		else if (players2.length < groupsVol) {
			players2.push(player);
			sum2 += player.pts;
		}
		else if (players1.length < groupsVol) {
			players1.push(player);
			sum1 += player.pts;
		}
	}
	return new Game(players1, players2)
}

function balanceFunction(){
	console.log("Balance!");
	nicknames = document.getElementById("team-balancer").getElementsByClassName("nickname-field");
	points = document.getElementById("team-balancer").getElementsByClassName("points-field")
	var players = [];
	for (var i = 0; i < 10; i++) {
		players[i] = new Player(nicknames[i].value, Number(points[i].value));
	}

	var thatGame = splitPlayers(players);
	for (i = 0; i < 5; i++) {
		document.getElementById("points-calculator").getElementsByClassName("nickname-field")[i].value = thatGame.players[0][i].nickname;
		document.getElementById("points-calculator").getElementsByClassName("points-field")[i].value = thatGame.players[0][i].pts;

		document.getElementById("points-calculator").getElementsByClassName("nickname-field")[5 + i].value = thatGame.players[1][i].nickname;
		document.getElementById("points-calculator").getElementsByClassName("points-field")[5 + i].value = thatGame.players[1][i].pts;
	}
}

function calculateWinnerFunction(){
	console.log("Calculate!");
	nicknames = document.getElementById("points-calculator").getElementsByClassName("nickname-field");
	points = document.getElementById("points-calculator").getElementsByClassName("points-field")
	var players = [];
	for (var i = 0; i < 10; i++) {
		players[i] = new Player(nicknames[i].value, Number(points[i].value));
	}

	var thatGame = new Game(players.slice(0,5), players.slice(5,10));
	document.getElementById("points-calculator").getElementsByClassName("team-name")[0].innerHTML = "<b>Avg: " + thatGame.avg[0] + " +" + winLoseCosts(thatGame.avg[0], thatGame.avg[1]) + "/-" + winLoseCosts(thatGame.avg[1],thatGame.avg[0]) + "</b>";
	document.getElementById("points-calculator").getElementsByClassName("team-name")[1].innerHTML = "<b>Avg: " + thatGame.avg[1] + " +" + winLoseCosts(thatGame.avg[1], thatGame.avg[0]) + "/-" + winLoseCosts(thatGame.avg[0],thatGame.avg[1]) + "</b>";
}

var balance_button_click = document.getElementById("balance-button");
balance_button_click.addEventListener("click", balanceFunction);

var calculate_button_click = document.getElementById("calculate-button");
calculate_button_click.addEventListener("click", calculateWinnerFunction);
