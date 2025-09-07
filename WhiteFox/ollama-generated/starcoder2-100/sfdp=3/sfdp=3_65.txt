
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(32, 64)
        self.key  = torch.nn.Linear(32, 64)
 
    def forward(self, query_tensor, key_tensor, value_tensor, scale_factor=None): # This line defines the scaling factor. By default, this parameter is None
        v1  = torch.matmul(query_tensor, key_tensor.transpose(-2, -1))
 
        if scale_factor != None:
            v2  = self.query(scale_factor).unsqueeze(0) * v1
            v3  = scaled_qk  # This line defines the scaling factor
        else:
            v2  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) * value_tensor
            dropout_qk = torch.nn.Dropout(p=dropout_p)
 
        return v2
 
# Initializing the model
m1  = Model()

