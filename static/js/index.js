class TriageForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        name: '',
        age: '',
        ageGroup: 0,
        birthday: '',
        gender: '',
        address: '',
        contactNumber: '',
        symptoms: {},
        comorbidities: {},
        travel: '',
        disposition: '',
        isForTesting: false,
        // metadata
        boothNum: 0,
        officer: 'Juan',
        timestamp: ''
    };
    // populate symptoms and comorbidites as set by interview specifications
    Object.entries(symptoms).map(
      ([_, item]) => this.state.symptoms[item.name] = false)
    Object.entries(comorbidities).map(
      ([_, item]) => this.state.comorbidities[item.name] = false)
    this.handleChange = this.handleChange.bind(this);
    this.handleCheckboxChange = this.handleCheckboxChange.bind(this);
    this.handleRadioChange = this.handleRadioChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
