from kubernetes import client, config
config.kube_config.load_kube_config(config_file="./kubeconfig.yaml")

class Kubernetes:

  def __init__(self):
    self.Connect = client.CoreV1Api()

  def ListNameSpace(self):
    data = []
    for ns in self.Connect.list_namespace().items:
      data.append(ns)
    return data

  def CreateNameSpace(self,name):
    body = client.V1Namespace()
    body.metadata = client.V1ObjectMeta(name=name)
    return self.Connect.create_namespace(body=body)

  def ListPods(self, ns):
    data = []
    for pod in self.Connect.list_namespaced_pod(namespace=ns).items:
      data.append(pod)
    return data


k = Kubernetes()
#print(k.ListNameSpace())
print(k.ListPods('kubeflow'))
