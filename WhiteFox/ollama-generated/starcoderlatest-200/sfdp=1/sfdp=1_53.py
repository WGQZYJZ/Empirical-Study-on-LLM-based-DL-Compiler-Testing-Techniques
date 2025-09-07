
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.key_projection = torch.nn.Linear(3, 64) # linear projection layer from (Batch Size x Key Depth x Query Width x Query Height) to 64 for key
        self.value_projection = torch.nn.Linear(256, 128) # linear projection layer from 256 to 128 for value
        self.query_projection = torch.nn.Linear(64, 256) # linear projection layer from 64 to 256 for query
 
        self.attention = torch.nn.Linear(320, 64) # linear projection layer from (Batch Size x Key Depth x Query Width x Query Height) to 64 for attention
        self.out = torch.nn.Linear(64, 10) # final fully connected layer with Softmax activation
 
    def forward(self, x):
        v1 = self.key_projection(x) # apply linear projection from (Batch Size x Key Depth x Query Width x Query Height) to 64 for key
        v2 = self.value_projection(v1) # apply linear projection from 256 to 128 for value
        v3 = self.query_projection(x) # apply linear projection from 64 to 256 for query
 
        attention = self.attention(torch.cat((v1, v2, v3), dim=1)) # concatenate the key, value and query embeddings
        attention = torch.nn.functional.softmax(attention, dim=-1) # apply softmax on the output of linear layer with 64 inputs to compute weights
        attention = torch.nn.functional.dropout(attention, p=dropout_p) # apply dropout before multiplication by value
        
        out = self.out(torch.mul(x, attention)) # multiply each input embedding element by their respective attention weighting value
 
        return out


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(20, 3, 64, 64)
