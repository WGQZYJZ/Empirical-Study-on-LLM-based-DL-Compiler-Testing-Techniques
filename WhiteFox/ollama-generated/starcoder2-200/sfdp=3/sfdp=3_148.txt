

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        scale = 1024. / math.sqrt(query.size(-1)) if args.scale else 1.0
        v1 = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        v2 = v1 * scale  # Scale the dot product by a factor
        v3 = torch.nn.functional.softmax(v2)  # Apply softmax to the scaled dot product
        v4 = value.matmul(v3)  # Compute the dot product of the value tensor and the resulting softmax output
	return v1, v2, v3, v4

# Initializing the model
m  = Model()

