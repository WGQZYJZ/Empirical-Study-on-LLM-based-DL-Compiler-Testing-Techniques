

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul  = torch.nn.functional.dropout

    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) 
        v2  = v1 * scale_factor
        v3  = v2.softmax(dim=-1)
        v4  = self.matmul(v3, p=dropout_p) # dropout
        return v4.matmul(value)


# Initializing the model