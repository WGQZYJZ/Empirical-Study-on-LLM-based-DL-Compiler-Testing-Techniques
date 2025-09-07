
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(128, 64)
        self.key = torch.nn.Linear(128, 64)
 
    def forward(self, q, k):
        # This code is an abbreviated form of the following pattern:
        # query = linear_layer(query).unsqueeze(-2)
        # key = linear_layer(key).unsqueeze(-1)
        # scaled_qk = torch.matmul(query, key.transpose(-2, -1)) * scale_factor
        # softmax_qk = scaled_qk.softmax(dim=-1)
        # output = torch.nn.functional.dropout(softmax_qk, p=dropout_p).matmul(value)
        query  = self.query(q).unsqueeze(-2) 
        key = self.key(k).unsqueeze(-1) 
        scaled_qk = torch.einsum('bqd,bj->bqjd', [query, key]) * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        output = torch.nn.functional.dropout(softmax_qk, p=dropout_p).matmul(value)
        return output
 

# Initializing the model
m = Model()

 # Inputs to the model
query  = torch.randn(64, 128, device=device, dtype=torch.float32) # This is a typical way of initialing inputs for self-attention mechanisms
key  = torch.randn(64, 128, device=device, dtype=torch.float32) # This is a typical way of initialing keys and values for multihead attention
__output__  = m(query, key)

 