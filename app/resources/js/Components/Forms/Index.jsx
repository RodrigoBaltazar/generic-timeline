import './Form.css'
import 'bootstrap/dist/css/bootstrap.min.css';



const Form = () => {
    return (

        <section>
            <form>
            <label>
                Title: <input name="title" />
            </label>
            <hr />
            <label>
                Description: <input name="description" />
            </label>
            <hr />
            <label>
                Duration: <input name="duration" />
            </label>
            <hr />
            <button type="button" class="btn btn-primary">
                Enviar
            </button>
            </form>
        </section>
    )
}

export default Form