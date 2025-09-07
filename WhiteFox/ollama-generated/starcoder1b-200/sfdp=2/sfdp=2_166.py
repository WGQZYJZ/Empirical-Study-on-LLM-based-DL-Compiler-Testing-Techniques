
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(d_model, d_k * 4)
 
    def forward(self, x):
        v = self.qkv(x)
        scale = v[..., :1].div(torch.sqrt(v[..., 1:] + epsilon))  # Compute the square root of each element
        dropout = torch.nn.functional.dropout(scale, p=dropout_p)  # Apply dropout to the inverse scale factor
        output = dropout.matmul(value)  # Compute the dot product of the scale and value
        return output


# Initializing the model
m = Model()


