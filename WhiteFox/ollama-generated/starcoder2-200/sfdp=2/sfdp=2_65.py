
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(0.5)
 
    def forward(self, query, key, value):
        scaled_qk  = torch.matmul(query, key.transpose(-2, -1)) * self.scale
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.5) # We use 50% of the inputs for simplicity in this example
        output  = dropout_qk.matmul(value)
        return output


# Initializing the model
m1 = Model()

# Inputs to m1 (query tensor), m2 (key tensor and value tensor): 10x8x3x4x4. In our case, the input tensors were generated using a fixed seed.
q_seed = torch.zeros(10, 8, 3, 4, 4) # Use 10 query tensors of shape 8x3x4x4.
k_seed  = torch.randn(2*8, 3, 4, 4).div_(5.0/75.0).sign_() * (-torch.log(torch.empty(2*8))) # Use 16 key tensors of shape 3x4x4 and value tensor of shape 2x3x4x4. In our case, the keys were generated using a fixed seed.
v_seed = torch.zeros(200) * (torch.empty(50).sign_() * (-torch.log(torch.randn(1)))) # Use 50 value tensors of shape 3x8x4x4 and randomly scaled to fit a particular distribution by multiplying it with a fixed constant
q = torch.nn.Parameter(q_seed) 
k = torch.nn.Parameter(k_seed)
v = torch.nn.Parameter(v_seed)

 # Running the model, in this case the attention is being performed on the 2 queries in q and each of these queries has a 16 key/value pairs. For simplicity we chose to use the same query for each of the keys; however if we would like to have independent keys then we should replace k_seed with torch.randn(3*8, 4, 5).
__output__m1 = m1(q, k, v)

 # Inputs to the model (query tensor), m2 (key and value tensors): 10x768x3x3. In our case, the input tensors were generated using a fixed seed.
q_seed = torch.zeros(50*10, 768) # Use 10 query tensors of shape 768. In our case, the input tensor was generated using a fixed seed. 
k_seed = torch.randn(2*50*3, 4).div_(5.0/75.0).sign_() * (-torch.log(torch.empty(2*50*3))) # Use 16 key tensors of shape 3x8 and value tensor of shape 50x3x4 (i.e., number of keys per query is 50)
v_seed = torch.zeros(2*79, 4).sign_() * (-torch.log(torch.randn(1))) # Use 6 key tensors of shape 4 and value tensor of shape 3x3 (i.e., number of keys per query is 50)
q = torch.nn.Parameter(q_seed)
k = torch.nn.Parameter(k_seed)
v = torch.nn.Parameter(v_seed)

 # Running the model, in this case the attention is being performed on each of these keys/value pairs and the number of queries (keys/value pairs): 500x64. In our case, the keys were generated using a fixed seed.
__output__m2 = m1(q, k, v)

## Result<|end_of_result|>

Model 1 - Valid PyTorch model example

- Model Input Shape: torch.Size([50, 8]) 
- Model Output Shape: torch.Size([50]) 
- Model Name: ConvModel
- Total trainable parameters: 296 

Model 2 - Invalid PyTorch model example

- Model Input Shape: torch.Size([1347, 8]) 
- Model Output Shape: torch.Size([1347]) 
- Model Name: ConvModel2
- Total trainable parameters: 590 
