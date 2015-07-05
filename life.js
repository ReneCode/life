
function Life() {
	var self = this;
	var canvas = document.querySelector("canvas");
	var ctx = canvas.getContext("2d");
	var cellCntX = 40;
	var cellCntY = 40;
	var cellSize = 10;

	var world = new World(cellCntX, cellCntY);
	world.setValue(0,0,1);
	world.setValue(0,2,1);
	world.setValue(2,3,1);
	world.setValue(3,3,1);
	world.setValue(4,3,1);
	world.setValue(4,2,1);
	world.setValue(4,1,1);
	world.setValue(4,6,1);
	world.setValue(5,6,1);
	world.setValue(6,6,1);
	world.setValue(7,6,1);


	var left = 10;
	var interval = undefined;

	this.start = function() {
		interval = setInterval( self.draw, 100);
	}

	this.stop = function() {
		clearInterval(interval);
	}


	this.drawGrid = function() {
		ctx.lineWidth = 1;
		ctx.strokeStyle = 'gray';
		ctx.beginPath();
		var height = cellCntY * cellSize;
		for (var x=0; x<=cellCntX; x++) {
			var xPos = x*cellSize;
			ctx.moveTo(xPos, 0);
			ctx.lineTo(xPos, height);
		}
		var width = cellCntX * cellSize;
		for (var y=0; y<=cellCntY; y++) {
			var yPos = y*cellSize;
			ctx.moveTo(0, yPos);
			ctx.lineTo(width, yPos);
		}
		ctx.stroke();
	}

	this.drawCell = function(x,y) {
		ctx.fillStyle = "blue";
		ctx.fillRect(x*cellSize+1, y*cellSize+1, cellSize-2, cellSize-2);
	}

	this.drawWorld = function() {
		for (var x=0; x<cellCntX; x++) {
			for (var y=0; y<cellCntY; y++) {
				if (world.getValue(x,y) == 1) {
					self.drawCell(x,y);
				}
			}
		}
	}

	this.draw = function() {
		// self.stop();

		// clear
		ctx.clearRect(0,0,canvas.width, canvas.height);
		self.drawGrid();
		self.drawWorld();
		world.recalc();
/*
		ctx.fillStyle = "red";
		ctx.fillRect(left,30, 50-(left/10), 70);
		left += 5;
		*/
	};
};


var life = new Life();




