<script>
class Vector {
  constructor(...components) {
    this.components = components
    this.res = { ...[components] }
    this.res.length = 0
  }
  // ...

  scaleBy(number) {
  	this.res = new Vector(
      ...this.components.map(component => component * number)
    )
  	return this;
  }
  
  
  dot({ components }) {
    this.res.dot = components.reduce((acc, component, index) => acc + component * this.components[index], 0)
  	return this
  }
  
  normalize() {
  	this.length()
    this.resnormalize = this.scaleBy(1 / this.len)
    return this
  }
  
  then(cb_func){
  	cb_func(this.res)
    return this
  }
}

const one = new Vector(1, 4)
new Vector(2, 2)
	.scaleBy(2)
    .then(display)
    
    
    
    
    
function display(data){
	console.log(data)
}
</script>
