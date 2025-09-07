
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self):
        t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device)
        t2 = convert_element_type(t1, dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model and printing the result of `forward` function in textual format:
m = Model()
out  = m()
print(out.__repr__()) # To be used to generate inputs for the analysis.

# Running the analysis
python pytorch_model_analyzer/analyze.py -model_class "Model" -inputs "out" -torch_path "<path-to-pytorch>" -torch_models "<path-to-pytorch-models>" -output_file "results.csv"

