
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        v0 = torch.randn(32, 64)
        
        # Input tensor to the model. Change this to create a different input for the model.
        x_new  = torch.randn(1, 3, 5, 5) # Create an arbitrary input to the model
 
        v1  = self.conv(x1) # Replace conv with self.conv to generate different patterns
        v2  = torch.sigmoid(v1) 
        v3  = v1 * v2
        return x_new, v0


# Initializing the model and setting input tensor to the model's forward method
m  = Model()
 

# Inputs to the model: a randomly generated tensor, and an arbitrary input for the model. These are needed as parameters to m(x1).  
x1  = torch.randn(32,64) # create random data for m(x1),  and also change this to try different inputs
x_new, v0  = m(x1)
 


# If you want to visualize the model:
 

# Visualizing the input to the model's forward method. This is a dummy input tensor of shape (128,) because our first argument is a placeholder for the output of the model.  
dummy_input  = torchviz.make_dot(x_new, params=dict())

# Saving the visualization as an image file. This will save your visualization in an img folder under your project's root directory.
dummy_input.render("Input_to_model", format="png")

