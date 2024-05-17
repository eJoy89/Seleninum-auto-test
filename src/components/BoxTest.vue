<template>

    <div class="box-container" :style="{ background: changeColour ? 'lightcoral' : 'red' }">
        {{ changeColour }}
    </div>
</template>

<script>
export default {
    props: {
        changeColour: {
            type: Boolean,
            default() {
                return true;
            }
        }
    }

}
</script>

<style scoped>
.box-container{
    width: 250px;
    height: 250px;
}
</style>