## **ML in production**

**0.) [DONE] Установите kubectl**

https://kubernetes.io/docs/tasks/tools/

**1.) [DONE] Разверните kubernetes. Вы можете развернуть его в облаке:**
- https://cloud.google.com/kubernetes-engine
- https://mcs.mail.ru/containers/
- https://cloud.yandex.ru/services/managed-kubernetes

Либо воспользоваться локальной инсталляцией
- https://kind.sigs.k8s.io/docs/user/quick-start/
- https://minikube.sigs.k8s.io/docs/start/

Напишите, какой способ вы избрали. Убедитесь, что кластер поднялся (kubectl cluster-info).  


------------------------------------------------------------------------------

Для разворачивания был использован https://cloud.google.com/kubernetes-engine

Install Google Cloud SDK (https://cloud.google.com/sdk). In command prompt:

```gcloud auth login```



Paste command from google

```gcloud container clusters get-credentials cluster-1 --zone us-central1-c --project quixotic-vent-....```

```kubectl cluster-info```

![Alt text](imgs/01_google_cloud_login.png?raw=true "kubectl cluster-info")

-------------------------------------------------------------------------------


<br/>
То же было сделано на локальной инсталляции (https://minikube.sigs.k8s.io/docs/start/). Однако для локальной инсталляции не хватило ресурсов довести дз до конца - диск C:\ забит под завязку, не удалось перенести выхлоп докера на другой диск. Поэтому на ней сделан только первый пункт, а далее на https://cloud.google.com/kubernetes-engine

Для локальной инсталляции:
 
From command propmpt:

Select drive to keep minikube configs (needs 20Gb of free space) via setting MINIKUBE_HOME enviromental variable:

```setx MINIKUBE_HOME X:\Kubernetes\.minikube```

Restart command prompt


Run:

```minikube start```

```kubectl cluster-info```

![Alt text](imgs/01_minikube_cluster_up.png?raw=true "kubectl cluster-info")

To clean all

```minikube delete --all --purge```

**2) [DONE] Напишите простой pod manifests для вашего приложения, назовите его online-inference-pod.yaml** (https://kubernetes.io/docs/concepts/workloads/pods/)
Задеплойте приложение в кластер (kubectl apply -f online-inference-pod.yaml), убедитесь, что все поднялось (kubectl get pods)
Приложите скриншот, где видно, что все поднялось
(4 балла)

------------------------------------------------------------------------------
Register on doeckerhub. In command prompt:

```docker logout```
```docker login```

Navigate to /online_inference folder:

```docker build -t greasygoose/online_inference:v1 .```

[DON'T MISS DOT AT THE END!!!]


Push docker image to your docker hub (on hub.docker.com create repository online_inference)

```docker push greasygoose/online_inference:v1```

Deploy manifest to cluster:

```kubectl apply -f online-inference-pod.yaml``` 

(specify correct path to greasygoose\kubernetes\online-inference-pod.yaml)

Check if everything is OK:

```kubectl get pods```

To delete pod:

```kubectl delete -f online-inference-pod.yaml```

or all pods:

```kubectl delete pods --all```

![Alt text](imgs/02_google_cloud_cluster_up.png?raw=true "kubectl cluster-info")

------------------------------------------------------------------------------

**2а) [DONE] Пропишите requests/limits и напишите зачем это нужно в описание PR**
закоммитьте файл online-inference-pod-resources.yaml
(2 балла)

------------------------------------------------------------------------------

=> При отсутствии ограничений на ресурсы контейнер может занять все ресурсы, доступные на ноде, на которой он запущен. 
Для более эффективной работы следует ограничивать запросы CPU и лимит CPU для контейнеров Pod'а, чтобы Pod попал в расписание запуска.

------------------------------------------------------------------------------

**3) [DONE] Модифицируйте свое приложение так, чтобы оно стартовало не сразу(с задержкой секунд 20-30) и падало спустя минуты работы.** 
Добавьте liveness и readiness пробы, посмотрите что будет происходить.
Напишите в описании -- чего вы этим добились.

Закоммититьте отдельный манифест online-inference-pod-probes.yaml (и изменение кода приложения)
(3 балла)

Опубликуйте ваше приложение(из ДЗ 2) с тэгом v2

------------------------------------------------------------------------------

```docker build -t greasygoose/online_inference:v2 .```
```docker push greasygoose/online_inference:v2```


```kubectl apply -f online-inference-pod-probes.yaml```
```kubectl get --watch pods```
```kubectl delete -f online-inference-pod-probes.yaml```

=> Readiness проба используется для проверки на готовность обрабатывать запросы. Liveness проба используется для проверки штатной работы: если приложение падает, контейнер перезапускается. 

![Alt text](imgs/03_google_cloud_liveleness_readiness.png?raw=true "kubectl cluster-info")

------------------------------------------------------------------------------

**4) [DONE] Создайте replicaset, сделайте 3 реплики вашего приложения.** 
(https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)

Ответьте на вопрос, что будет, если сменить докер образа в манифесте и одновременно с этим 
а) уменьшить число реплик
б) увеличить число реплик.
Поды с какими версиями образа будут внутри будут в кластере?
(3 балла)
Закоммитьте online-inference-replicaset.yaml

------------------------------------------------------------------------------

## Experiment #1:

```kubectl apply -f online-inference-replicaset.yaml```

```kubectl get pods```

Decrease replicas number, change version to v1

```kubectl apply -f online-inference-replicaset.yaml```
```kubectl get pods```

Stop. Delete all pods.

При изменении версии образа в манифесте и одновременно с этим уменьшении кол-ва реплик старые pod'ы отключаются до достижения нового уменьшенного числа.
Было: 3 реплики версии v2. 
Уменьшила число реплик до 2 и изменила версию на v1.
Стало: 2 реплики версии v2.


Apply_3_replicas:

![Alt text](imgs/04a_google_apply3.png?raw=true "Apply_3_replicas")

Apply_2_replicas:

![Alt text](imgs/04b_google_apply2.png?raw=true "Apply_2_replicas")
![Alt text](imgs/04_google.png?raw=true "kubectl cluster-info")

## Experiment #2:

```kubectl apply -f online-inference-replicaset.yaml```
```kubectl get pods```

Increase replicas number, change version to v1

```kubectl apply -f online-inference-replicaset.yaml```
```kubectl get pods```
Stop. Delete all pods.

При изменении версии образа в манифесте и одновременно с этим увеличении кол-ва реплик добавляются новые pod'ы до достижения нового увеличенного числа.
Было: 3 реплики версии v2. 
Увеличила число реплик до 4 и изменила версию на v1.
Стало: 3 реплики версии v2, 1 реплика версии v1. 


Apply_3_replicas:

![Alt text](imgs/04c_google_apply3.png?raw=true "Apply_3_replicas")

Apply_4_replicas:

![Alt text](imgs/04d_google_apply4.png?raw=true "Apply_2_replicas")
![Alt text](imgs/04e_google.png?raw=true "kubectl cluster-info")

------------------------------------------------------------------------------

**5) [DONE] Опишите деплоймент для вашего приложения.**  
(https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
Играя с параметрами деплоя(maxSurge, maxUnavaliable), добейтесь ситуации, когда при деплое новой версии 
a) Есть момент времени, когда на кластере есть как все старые поды, так и все новые (опишите эту ситуацию) (закоммититьте файл online-inference-deployment-blue-green.yaml)
б) одновременно с поднятием новых версии, гасятся старые (закоммитите файл online-inference-deployment-rolling-update.yaml)
(3 балла)

------------------------------------------------------------------------------
Для достижения эффекта а) ставим запрет на отключение старых pod'ов, пока не запустятся новые pod'ы:

maxSurge=100%,  maxUnavaliable=0%

Соответственно, в момент, когда запустились все новые pod'ы, а старые еще не отключились,  в ноде будет полный набор.


```kubectl apply -f online-inference-deployment-blue-green.yaml```

![Alt text](imgs/05_blue_green.png?raw=true "05_blue_green")


Для достижения эффекта б) ставим после создания одного нового pod'а отключение одного старого:

 maxSurge=50%, maxUnavaliable=50%

```kubectl apply -f online-inference-deployment-rolling-update.yaml```

![Alt text](imgs/05_rolling_update.png?raw=true "05_rolling_update")

------------------------------------------------------------------------------

**[NOT IMPLEMENTED] Бонусные активности:**
Установить helm и оформить helm chart, включить в состав чарта ConfigMap и Service. -- 5 баллов








