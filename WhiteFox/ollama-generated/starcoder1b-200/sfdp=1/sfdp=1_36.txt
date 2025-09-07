
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(3, 5)
        self.key   = torch.nn.Linear(4, 5)
        self.value = torch.nn.Linear(5, 8)
 
    def forward(self, x1, x2):
        kq = self.query(x1).unsqueeze(-1) # Query is a linear layer with input of shape (batch_size, 3, sequence_length, embed_dim)
        vk = self.key(x2).unsqueeze(0)     # Key is a linear layer with input of shape (batch_size, sequence_length, embed_dim)
        v = torch.bmm(qk, vk).squeeze(-1)  # The dot product of query and key tensors is computed
        ske = scaled_softmax(v, inv_scale_factor=self.d_k) # Apply softmax to the dot product of the query and key tensors
        v = dropout(ske, p=dropout_p)                # Apply dropout on the softmax output
        o  = self.value(v).squeeze()           # The dropout output is multiplied by the value tensor, then squeezed (batch_size, sequence_length, embed_dim)
        return o


# Initializing the model
m = Model()

