
class Model(torch.nn.Module):
    def __init__(self, hidden_dim=3072):
        super().__init__()
        self.query = torch.nn.Linear(hidden_dim * 4, hidden_dim) # Initialize a linear layer for the query vector
        self.key = torch.nn.Linear(hidden_dim * 8, hidden_dim) # Initialize a linear layer for the key vector
 
        self.attn_mask = torch.triu(torch.ones(7, 7), diagonal=1).unsqueeze(0) # Create an upper triangular matrix to represent the attention mask
        self.dropout = torch.nn.Dropout(p=0.35)
 
    def forward(self, x):
        vq = self.query(x[:, :hidden_dim]) # Compute the query vector for the 7 * hidden size inputs
        vk = self.key(x[:, -2 * hidden_dim:]) # Compute the key vector for the 8th block of 4 * hidden size inputs
 
        # Compute the dot product of the query and key, add a diagonal mask to it to make the attention mechanism more powerful, 
        # and then apply dropout on the attention weights.
        # Add the output of softmax back onto the query and value.
        qk = torch.einsum('bhid,bhid->bidh', vq, vk) + self.attn_mask 
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = self.dropout(attn_weight)
 
        output =  torch.einsum("bidh,bhhd->bhi", attn_weight, x[:, -3 * hidden_dim:])
 
        return output


# Initializing the model
m = Model()
 
# Input to the model (in batch size of 4 with a total length of 18)
x = torch.rand(4, 7 + 6, 50) # The 3rd block contains 50 elements, and the 2nd block is 300
 
# Forward pass to the model
