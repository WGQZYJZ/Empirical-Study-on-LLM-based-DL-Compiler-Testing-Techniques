The model should contain the following pattern:
This pattern characterizes scenarios where a convolution layer (`torch.nn.ConvXd` or `torch.nn.Conv2d`) is followed by a batch normalization layer  (`torch.nn.BatchNormXd` or `torch.nn.BatchNorm2d`). The output of the convolution layer is used as the input to the batch normalization layer.

The `fuse_conv_bn` optimization is triggered when the convolution and batch normalization layers are in evaluation mode (not in training mode), and the batch normalization layer is tracking running statistics. 

After the optimization, the convolution and batch normalization layers are fused into a single convolution layer, and the batch normalization layer is removed from the graph. If the output of the convolution layer is used by other nodes, the optimization will not be performed.

The optimization also applies to the functional API equivalent of the above pattern, where `torch.nn.functional.convXd` or `torch.nn.functional.batch_norm` are used instead of the module API. The constraints for the functional API pattern are similar to the module API pattern.

# Performance test
The input should be a valid model example. For the testing, the model can either be implemented by yourself, or you need to use `torchserve`. We provide two ways to verify the inference results: (1) by comparing the predicted and actual values obtained during the inferences using the `tensorrt_api` tool provided by Intel and (2) by comparing the CPU performance.

## Verify the prediction
Please run the following command under the source code directory where your model resides, and enter the following command to verify the output result:
You can also get the predicted output results from `model.onnx` and compare it to the actual outputs in the `actual_outputs/model-000100`. The comparison of the two predictions is as follows:

 | model   | predict    | actual   |
 | ---     | ---        | ---      |
 |  model  | conv_output| input_tensor.permute(2,3,1) * linear_result + batchnorm_result |
 
## Verify the inference time
We also provide a script to evaluate inferences time of `trtexec` and PyTorch models by following the instructions in the [README](/README.md). The two APIs are used to obtain inference times: (1) by using PyTorch API to perform inference with dynamic batch sizes, and (2) by using `tensorrt_api`. 

For (1), the script should be executed as follows:
The script should be executed as follows:
The `trtexec` tool provides the `--time` option to get the inference time for all the models provided by Intel. For example, we can obtain the prediction time and inference time of a model:

For (2), the script should be executed as follows:
The script should be executed as follows:
