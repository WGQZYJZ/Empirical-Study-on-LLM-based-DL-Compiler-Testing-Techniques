
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Parameter(
            torch.rand(2, 10, 5) * 3 # Initialize the query parameter to a random value of size [2 x 10 x 5] with scale 3
        )
        self.key  = torch.nn.Parameter(
            torch.rand(4, 8, 5) * 7 # Initialize the key parameter to a random value of size [4 x 8 x 5] with scale 7
        )
        self.value  = torch.nn.Parameter(
            torch.rand(32, 600, 1024) * 1/np.sqrt(600*1024) # Initialize the value parameter to a random value of size [32 x 600 x 1024] with scale sqrt(600*1024)/2
        )
        self.scale_factor = torch.nn.Parameter(
            torch.tensor([3978.5], dtype=torch.float) # Initialize the scale factor parameter to a constant value of size [1 x 1] with value 3978.5
        )
        self.dropout_p  = torch.nn.Parameter(
            0.4, requires_grad=False
        )
 
    def forward(self, query):
        vq  = torch.nn.functional.linear(query, key) # Compute the dot product of a randomly generated query and the key
        scaled_vq  = vq / self.scale_factor # Scale the dot product by an inverse scale factor that is set to constant value 3978.5
        svp  = scaled_vq.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropouted_svp  = torch.nn.functional.dropout(svp, p=self.dropout_p, training=self.training) # Apply dropout to the softmax output
        vout = dropouted_svp.matmul(value) # Compute the dot product of the dropout output and a randomly generated value
        return vout


# Initializing the model
m  = Model()


# Inputs to the model
query  = torch.randn(1, 10, 5) # A randomly generated query of size [1 x 10 x 5] with mean and standard deviation 0 and 3


