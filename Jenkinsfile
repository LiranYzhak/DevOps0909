properties([pipelineTriggers([pollSCM('* * * * * ')])])
node {
    stage("clone"){
        git "https://github.com/LiranYzhak/DevOps0909"
}
    stage("show files"){
        sh "ls -l"
    }
}
