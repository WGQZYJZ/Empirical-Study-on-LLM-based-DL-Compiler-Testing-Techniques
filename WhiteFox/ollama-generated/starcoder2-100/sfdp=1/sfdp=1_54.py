
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scale = torch.tensor([0.1]).to('cuda') # Setting the scaling factor to 0.1
        
        # Applying the dot product of a query and key tensor is computed. 
        v_qk = torch.matmul(query, key) 
        
        # Scales by 0.1.
        v_scaled = v_qk / scale
            
        # Computes softmax on a -2 dimension.
        v_softmax = scaled_qk.softmax(-2) 
        
        # Apply dropout to the dot product of the query and key tensor.
        # The probability of each element being set zero is equal to p, 
        # where p is set to the default value in the PyTorch implementation: 0.1.
        v_dropout = torch.nn.functional.dropout(softmax, p=0.1)
        
        # Computes dot product of dropout tensor and value tensor.
        # Computes dot product of dropout tensor and value tensor.
        v6  = v2 * v5
        return v6
# Initializing the model.
m = Model()

