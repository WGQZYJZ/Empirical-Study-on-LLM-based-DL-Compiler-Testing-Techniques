
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        	v = torch.nn.functional.dropout(x1, 0.5)  # Apply dropout to the input tensor
	        t2 = torch.rand_like(v, None) # Generate a random number and fill it with None.
	        return v, t2


# Initializing the model