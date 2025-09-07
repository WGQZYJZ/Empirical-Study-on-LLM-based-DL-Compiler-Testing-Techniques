
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, n_head):
        super().__init__()
        self.query = torch.nn.Linear(512, 384)
        self.key = torch.nn.Linear(512, 384)
        self.value = torch.nn.Linear(512, 384)
 
        self.fc_out = torch.nn.Linear(384 * n_head, 512)
 
    def forward(self, q, k, v):
        batch_size, n_q, c = q.shape
        # Apply linear transformation to the query and key before concatenation
        # Concatenate the two representations for each attention head
        e = torch.cat((q, k), dim=1)
        # Compute output from the intermediate layer
        e = self.query(e).reshape(batch_size, -1, n_head, 384)
 
        e = self.key(e).reshape(batch_size, -1, n_head, 384)
        v = self.value(v).reshape(batch_size, -1, n_head, 384)
 
        # Compute softmax on the output and scale to prevent numerical issues
        e = torch.einsum('bnqhwc,bncwht->bnqhwt', [e, v])
        attention = F.softmax(e, dim=-1)

        scaled_attention = attention * 0.25

        output = torch.einsum('bnqhwt,bncwhd->bnqhd', [scaled_attention, v])
        # Concatenate the intermediate and output layers
        return self.fc_out(output).reshape(batch_size, -1)
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.multi_head = MultiHeadAttention(n_head=8)
 
    def forward(self, x1):
        attention = self.multi_head(x1[0], x1[1], x1[2])
        # Replace the `pass` statement in the below code to pass input through the transformer
        # Pass all of the input data through the transformer layers and get an output that contains
        # the final representation of each batch item.
        return attention
# Initializing the model
m = Model()


# Inputs to the model
x1 = (torch.randn(1, 3, 64, 64), torch.randn(1, 3, 64, 64), torch.randn(1, 3, 64, 64))
