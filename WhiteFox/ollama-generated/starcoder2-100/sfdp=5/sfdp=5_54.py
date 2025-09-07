
class Model(torch.nn.Module):
    def __init__(self, hparams):
        super().__init__()

        self._output = torch.nn.Linear(1603840, 7)
 
    def forward(self, x1):
        v2 = x1 @ key_vec  # Compute the dot product of the query and key, and scale it
        v2 = v2 + attn_mask  # Add the attention mask to the scaled dot product
        v3 = torch.softmax(v2, dim=-1)  # Apply softmax to the result
        v4 = torch.dropout(v3, dropout_p, True)  # Apply dropout to the softmax output
        v5 = attn_weight @ value  # Compute the dot product of the dropout output and the value
        return self._output(v5)


# Initializing the model
m  = Model(hparams)

# Input tensor to the model. The shape is [2, 4, 8] because of broadcasting. 
x1  = torch.zeros([327680, 1])
x2  = torch.arange(shape=[327680], device="cuda", dtype=torch.int) + 5

