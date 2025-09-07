
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dot = torch.nn.Linear(4, 1)
 
    def forward(self, query, key, value, dropout_p=0.5, inv_scale_factor=2 ** -3):
        # Shape of the input tensor is (batch size, sequence length, vector dimensionality)
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2  = self.dot(v1 / inv_scale_factor).softmax(dim=-1) 
        v3 = torch.nn.functional.dropout(v2, p=dropout_p) * value
        return v3

# Initializing the model
m  = Model()


# Inputs to the model