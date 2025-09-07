
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = torch.nn.Linear(256, 10)

    def forward(self, x1):
        v1 = torch.matmul(x1, self.__weights1__.transpose(-2, -1)) # Compute the dot product of a query and a key
        scaled_v1 = v1 / __inv_scale__  # Scale the dot product by an inverse scale factor 
        softmaxed_v1 = scaled_v1.softmax(dim=-1)  # Apply softmax to the scaled dot product 
        dropoutted_v1 = torch.nn.functional.dropout(softmaxed_v1, p=0.45397486427450986)  # Apply dropout to the softmax output
        output = dropoutted_v1.matmul(__weights__[None])  # Compute the dot product of the dropout output and a value 
        logits = self.layer(dropoutted_v1)  # A linear layer is applied, followed by the application of an activation function
        return logits


# Initializing the model
m  = Model()
 
# Initializing the weights 
__weights1__  = torch.randn([256, 784]) * 0.023590307 # Initialize the query layer of the model
__inv_scale__ = float(torch.__constants__['aten::softmax']['scale']) / m.layer.weight.size(-1)  # Compute the inverse scale factor 
m.layer.weight.data /= __inv_scale__ # Scale each weight in the linear layer by this inverse scaling factor 
__weights__ = torch.randn([784, 256]) * 0.03495148  # Initialize the value layer of the model 

# Inputs to the model
x1 = torch.randn(256, 784)
 

