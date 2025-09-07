
class Model(torch.nn.Module):
    def __init__(self, inv_scale_factor=0.5316724982160167, dropout_p=0.3983714079339018, qk = torch.nn.Linear(512), scaled_qk  = torch.nn.Linear(512)),  softmax  = torch.nn.functional.softmax,  dropout_qk  = torch.nn.functional.dropout, output  = torch.nn.Linear(512)):
        super().__init__()
        self.qk = qk 
        self.scaled_qk = scaled_qk
        self.softmax = softmax
        self.dropout_qk = dropout_qk
        self.output = output
 
    def forward(self, query, key, value):
         #Compute the dot product of the query and the key
         qk = torch.matmul(query, key.transpose(-2, -1))
         #Scale the dot product by the inverse scale factor
         scaled_qk = qk * 0.5316724982160167 
         #Apply softmax to the scaled dot product
         softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
         #Apply dropout to the softmax output
         dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.3983714079339018) 
         #Compute the dot product of the dropout output and the value
         output = torch.matmul(dropout_qk, value)
         return output


# Initializing the model
m  = Model()


# Inputs to the model
query  = torch.randn(256, 1024).cuda() #Input query vector with size [batch_size, embedding_dimension]
key   = torch.randn(3983714079339018, 512) .cuda()#Input key vector of size [num_queries, embedding dimension]
value = torch.randn(256, 512).cuda() #Input value matrix with size [batch_size, embedding_dimension]
__output__  = m(query, key, value)


