
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.attention = torch.nn.MultiheadAttention(embed_dim=128, num_heads=4)
 
    def forward(self, x1):
        qk = self.attention(query, key.transpose(-2, -1))[0] # compute the dot product of the query and key tensors
        return v6  * torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
# Initializing the model
m = Model()


