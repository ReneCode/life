// World


function World(cntX, cntY) {
	var self = this;
	var countX = cntX;
	var countY = cntY;

	var field = [];
	var logic = logic = { 0:[0,0],1:[0,0],2:[0,1],3:[1,1], 4:[0,0], 5:[0,0], 6:[0,0], 7:[0,0], 8:[0,0] }

	for (var x=0; x<countX; x++) {
		var row = [];
		for (var y=0; y<countY; y++) {
			row.push(0);
		}
		field.push(row);
	}

	this.checkIndex = function(x,y) {
		return (x >= 0  &&  x < countX  &&
				y >= 0  &&  y < countY);
	}

	this.getValue = function(x,y) {
		if (!self.checkIndex(x,y)) {
			return undefined;
		}
		return field[x][y];
	}

	this.setValue = function(x,y,val) {
		if (!self.checkIndex(x,y)) {
			return undefined;
		}
		field[x][y] = val;
	}



	this.countNeighbours = function(xMe,yMe) {
		var sum = 0;
		for (var x=xMe-1; x<=xMe+1; x++) {
			for (var y=yMe-1; y<=yMe+1; y++) {
				// do not count myself
				if (!(x==xMe && y==yMe)) {
					var i=x;
					var j=y;
					// flip over at the border of the world
					if (i<0) {
						i = countX-1;
					}
					if (i >= countX) {
						i = 0;
					}
					if (j<0) {
						j=countY-1;
					}
					if (j>= countY) {
						j = 0;
					}
					sum += field[i][j];
				}
			}
		}
		return sum;
	}

	this.recalc = function() {
		var neighbours = []
		for (var x=0; x<countX; x++) {
			var row = [];
			for (var y=0; y<countY; y++) {
				var countNeighbour = self.countNeighbours(x,y);
				row.push(countNeighbour);
			}
			neighbours.push(row);
		}		

		for (var x=0; x<countX; x++) {
			for (var y=0; y<countY; y++) {
				var newValue = logic[ neighbours[x][y] ][ field[x][y] ];
				field[x][y] = newValue;
			}
		}
	}



}