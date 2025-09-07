
import torch  # We should have torch.nn imported here to avoid confusion with our model class

class Model(torch.nn.Module):
    def __init__(self, inv_scale_factor=0.167):
        super().__init__()
        self._dropout = 0.5
    
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk / inv_scale_factor # Scale the dot product by the inverse scale factor 
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self._dropout) # Apply dropout to the softmax output 
        output = dropout_qk @ value  # Compute the dot product of the dropout output and the value tensor 
        return output

# Initializing the model
model  = Model()


# Inputs for the model 
query1  = torch.randn(2, 3)  
key1    = torch.randn(3, 4)
value1  = torch.randn(10, 3, 5)

output1 = model(query1, key1, value1)

query2  = torch.randn(3, 7)  # Query shape has to be (batch_size x sequence length), whereas key and value are 
                             # usually of shape (sequence length x batch_size x number_of_features)  
key2    = torch.randn(4, 500, 128)
value2  = torch.randn(3, 500, 768)
 
output2 = model(query2, key2, value2)

