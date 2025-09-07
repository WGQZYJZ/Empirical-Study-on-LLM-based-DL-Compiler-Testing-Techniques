
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query1, key1, value1, query2=None, key2=None, value2=None):
        v1  = torch.matmul(query1, key1.transpose(-2, -1))
        v3  = v1 / inv_scale_factor # Inverse scaling factor is defined as 0.7978845608028654 in the paper
        v4  = torch.nn.functional.dropout(torch.nn.functional.softmax(v3, dim=-1), p=dropout_p)
        v5  = v4 * value1
 
        if query2 is not None and key2 is not None and value2 is not None:
            v6  = self._matmul(query2, key2.transpose(-2, -1)) # This method calls `torch.matmul` directly without applying scaling factor to the dot product
            v7  = torch.nn.functional.dropout(v5 + v6) # This addition is a bit different from the pattern above. The dropout of the addition is applied after scaling by an inverse scale factor, not before it
        else:
            v7  = torch.nn.functional.softmax(torch.div(query1 @ query2, inv_scale_factor))

        return v5

# Initializing the model
m  = Model()

 # Inputs to the model
query1  = torch.randn(8, 64)
key1   = torch.randn(8, 32)
value1 = torch.randn(8, 32)

 # Initial prediction of the model with dropout=0 and query2 is not provided
__output__  = m(query1, key1, value1)

 
# Prediction of the model after dropout=0
query1_dropped   = torch.nn.functional.dropout(query1, p=dropout_p) # Dropout 0.5
key1_dropped     = torch.nn.functional.dropout(key1, p=dropout_p)
value1_dropped   = torch.nn.functional.dropout(value1, p=dropout_p)
__output2__      = m(query1_dropped, key1_dropped, value1_dropped).shape

 # Prediction of the model after dropout=0 and query2 is provided as inputs for `Model` class
query2  = torch.randn(8, 64)
key2   = torch.randn(8, 32)
value2 = torch.randn(8, 32)
  # Input tensors to the model
x1     = query1 + query2 # Addition of two inputs with dropout=0.5 for each input
x2     = key1 + key2    # The same as above but for keys and values instead of queries
x3     = value1        # Same as above but for values instead of queries
x4     = torch.nn.functional.dropout(torch.nn.functional.softmax(v5, dim=-1), p=dropout_p)
x5     = v7
__output2__  = m(query1+query2, key1 +key2, value1).shape

# Prediction of the model after dropout=0.4 and query2 is provided as inputs for `Model` class
query2_dropped   = torch.nn.functional.dropout(torch.nn.functional.softmax(v5+ v6 * 3), p=dropout_p) # Dropout 1/3 for the dropout of addition is used here, not 0.4 as in the first run
__output2__     = m(query1 + query2_dropped, key1 +key2, value1).shape
